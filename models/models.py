from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, Boolean, JSON
from datetime import datetime

metadata = MetaData()

role = Table(
    'roles',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('permissions', JSON),
)

user = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String, nullable=False),
    Column('registered_at', TIMESTAMP, default=datetime.utcnow),
    Column('role_id', Integer, ForeignKey('roles.id')),
    Column('email', String(length=320), unique=True, index=True, nullable=False),
    Column('hashed_password', String(length=1024), nullable=False),
    Column('is_active', Boolean, default=True, nullable=False),
    Column('is_superuser', Boolean, default=False, nullable=False),
    Column('is_verified', Boolean, default=False, nullable=False)
)