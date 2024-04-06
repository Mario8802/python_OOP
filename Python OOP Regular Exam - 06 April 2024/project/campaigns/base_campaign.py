from abc import ABC, abstractmethod

class BaseCampaign(ABC):
    _campaign_ids = set()

    def __init__(self, campaign_id: int, brand: str, budget: float, required_engagement: float):
        self._validate_campaign_id(campaign_id)
        self._campaign_id = campaign_id
        self.brand = brand
        self.budget = budget
        self.required_engagement = required_engagement
        self.approved_influencers = []

    @property
    def campaign_id(self) -> int:
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, value: int) -> None:
        self._validate_campaign_id(value)
        self._campaign_id = value

    @staticmethod
    def _validate_campaign_id(campaign_id: int) -> None:
        if not isinstance(campaign_id, int) or campaign_id <= 0:
            raise ValueError("Campaign ID must be a positive integer greater than zero.")
        if campaign_id in BaseCampaign._campaign_ids:
            raise ValueError(f"Campaign with ID {campaign_id} already exists. Campaign IDs must be unique.")
        BaseCampaign._campaign_ids.add(campaign_id)

    @abstractmethod
    def check_eligibility(self, engagement_rate: float) -> bool:
        pass
