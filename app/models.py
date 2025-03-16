from sqlalchemy import Column, String, Boolean, Float, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, declarative_base
import uuid
import datetime

Base = declarative_base()  # Ensure Base is correctly defined

class ScamClassification(Base):
    """Stores scam classification results."""
    __tablename__ = "scam_classifications"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    message_text = Column(String, nullable=False)
    is_scam = Column(Boolean, nullable=False)
    confidence = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class ScamExplanation(Base):
    """Stores AI-generated scam explanations and user questions."""
    __tablename__ = "scam_explanations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    message_id = Column(UUID(as_uuid=True), ForeignKey("scam_classifications.id"), nullable=False)
    question = Column(String, nullable=True)  # NULL means default explanation
    response = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    scam_classification = relationship("ScamClassification", backref="explanations")
