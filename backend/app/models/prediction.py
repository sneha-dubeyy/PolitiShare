from sqlalchemy import Column, String, Boolean, DateTime, Text, ForeignKey, Float
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base
import uuid

class Prediction(Base):
    __tablename__ = "predictions"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    survey_id = Column(UUID(as_uuid=True), ForeignKey("surveys.id", ondelete="CASCADE"))
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"))
    predicted_party = Column(String(50), nullable=False)
    confidence_score = Column(Float, nullable=False)
    prediction_probabilities = Column(JSONB, nullable=False)
    model_version = Column(String(50), nullable=False)
    feature_importance = Column(JSONB)
    explanation = Column(Text)
    is_shared = Column(Boolean, default=False)
    share_anonymously = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    survey = relationship("Survey", backref="predictions")
    user = relationship("User", backref="predictions")
