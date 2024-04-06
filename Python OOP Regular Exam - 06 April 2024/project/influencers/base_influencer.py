from abc import ABC, abstractmethod
from project.campaigns.base_campaign import BaseCampaign  # Import the BaseCampaign class


class BaseInfluencer(ABC):
    def __init__(self, username: str, followers: int, engagement_rate: float):
        self._username = None
        self._followers = None
        self._engagement_rate = None
        self._campaigns_participated = []

        self.username = username
        self.followers = followers
        self.engagement_rate = engagement_rate

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not value.strip():
            raise ValueError("Username cannot be empty or consist only of whitespace!")
        self._username = value

    @property
    def followers(self):
        return self._followers

    @followers.setter
    def followers(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Followers must be a non-negative integer!")
        self._followers = value

    @property
    def engagement_rate(self):
        return self._engagement_rate

    @engagement_rate.setter
    def engagement_rate(self, value):
        if not 0.0 <= value <= 5.0:
            raise ValueError("Engagement rate should be between 0 and 5.")
        self._engagement_rate = value

    @property
    def campaigns_participated(self):
        return self._campaigns_participated

    @abstractmethod
    def calculate_payment(self, campaign: BaseCampaign):
        pass

    @abstractmethod
    def reached_followers(self, campaign_type: str):
        pass

    def display_campaigns_participated(self):
        if not self.campaigns_participated:
            return f"{self.username} has not participated in any campaigns."

        campaigns_info = ""
        for campaign in self.campaigns_participated:
            reached_followers = self.reached_followers(campaign.__class__.__name__)
            campaigns_info += (f"\n  - Campaign ID: {campaign.campaign_id}, Brand: {campaign.brand},"
                               f" Reached followers: {reached_followers}")

        return f"{type(self).__name__} :) {self.username} :) participated in the following campaigns:{campaigns_info}"
