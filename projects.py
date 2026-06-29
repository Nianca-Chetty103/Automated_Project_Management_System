from sqlalchemy import Column, String, Enum, ForeignKey, DateTime
from database import Base
import enum

class Priority(enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"

class TaskStatus(enum.Enum):
    backlog = "backlog"
    in_progress = "in_progress"
    review = "review"
    done = "done"

class Task(Base):
    __tablename__ = "tasks"
    id          = Column(String, primary_key=True)
    title       = Column(String)
    description = Column(String)
    status      = Column(Enum(TaskStatus), default=TaskStatus.backlog)
    priority    = Column(Enum(Priority), default=Priority.medium)
    assignee_id = Column(String, ForeignKey("users.id"))
    project_id  = Column(String, ForeignKey("projects.id"))
    github_pr   = Column(String, nullable=True)  # linked PR URL
    due_date    = Column(DateTime, nullable=True)
