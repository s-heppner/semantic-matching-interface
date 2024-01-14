from typing import List

from pydantic import BaseModel


class SemanticMatchingServiceInformation(BaseModel):
    """
    The information a semantic matching service provides about itself,
    so that a client knows how to formulate the query
    """
    # (s-heppner 2023-04-11):
    # Note, that this is not yet final and subject to very much change
    matching_method: str
    matching_algorithm: str
    required_parameters: List[str]
    optional_parameters: List[str]


class BaseResponse(BaseModel):
    """
    The base response with the attributes all the other responses have in
    common.

    :cvar matching_method: The method used for the matching. For example:
        "NLP" for a semantic matching service using NLP
    :cvar matching_algorithm: The precise algorithm used for the matching
        In the above example, this would be the name of the model
    """
    matching_method: str
    matching_algorithm: str


class MatchObjectsMatchingResponse(BaseResponse):
    """
    The result of a successful `semantic_match_objects`.
    """
    matching_score: float
