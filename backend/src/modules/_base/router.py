"""
src/modules/_base/router.py
────────────────────────────
Generic CRUD router factory.

Usage:
    from src.modules._base.router import make_crud_router
    router = make_crud_router(
        model=SleepLog,
        create_schema=SleepLogCreate,
        read_schema=SleepLogRead,
        module_name="sleep",
    )

This generates:
    GET  /entries          → list with pagination
    POST /entries          → create
    GET  /entries/{id}     → get one
    DELETE /entries/{id}   → delete
    GET  /summary          → aggregated stats
"""
from typing import Type, TypeVar
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from pydantic import BaseModel

from src.dependencies import get_db
from src.modules._base.schema import ModuleSummary

ModelT = TypeVar("ModelT")
CreateSchemaT = TypeVar("CreateSchemaT", bound=BaseModel)
ReadSchemaT = TypeVar("ReadSchemaT", bound=BaseModel)


def make_crud_router(
    model: Type,
    create_schema: Type[BaseModel],
    read_schema: Type[BaseModel],
    module_name: str,
) -> APIRouter:
    router = APIRouter()

    @router.get("/entries", response_model=list[read_schema])
    def list_entries(
        limit: int = Query(20, le=100),
        offset: int = Query(0, ge=0),
        user_id: str = Query("demo-user"),
        db: Session = Depends(get_db),
    ):
        return (
            db.query(model)
            .filter(model.user_id == user_id)
            .order_by(model.created_at.desc())
            .offset(offset)
            .limit(limit)
            .all()
        )

    @router.post("/entries", response_model=read_schema, status_code=201)
    def create_entry(payload: create_schema, db: Session = Depends(get_db)):
        entry = model(**payload.model_dump())
        db.add(entry)
        db.commit()
        db.refresh(entry)
        return entry

    @router.get("/entries/{entry_id}", response_model=read_schema)
    def get_entry(entry_id: str, db: Session = Depends(get_db)):
        entry = db.query(model).filter(model.id == entry_id).first()
        if not entry:
            raise HTTPException(status_code=404, detail="Entry not found")
        return entry

    @router.delete("/entries/{entry_id}", status_code=204)
    def delete_entry(entry_id: str, db: Session = Depends(get_db)):
        entry = db.query(model).filter(model.id == entry_id).first()
        if not entry:
            raise HTTPException(status_code=404, detail="Entry not found")
        db.delete(entry)
        db.commit()

    @router.get("/summary", response_model=ModuleSummary)
    def get_summary(
        user_id: str = Query("demo-user"),
        db: Session = Depends(get_db),
    ):
        entries = db.query(model).filter(model.user_id == user_id).all()
        last = max((e.created_at for e in entries), default=None)
        return ModuleSummary(
            module=module_name,
            entry_count=len(entries),
            last_entry_at=last,
            summary_data={},   # TODO: each module overrides this with real aggregations
        )

    return router
