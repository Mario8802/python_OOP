from project.influencers.base_influencer import BaseInfluencer
from project.campaigns.base_campaign import BaseCampaign

class PremiumInfluencer(BaseInfluencer):
    def __init__(self, username: str, followers: int, engagement_rate: float):
        super().__init__(username, followers, engagement_rate)
        self.payment_percentage = 0.85

    def calculate_payment(self, campaign: BaseCampaign) -> float:
        payment = campaign.budget * self.payment_percentage
        return payment

    def reached_followers(self, campaign_type: str) -> int:
        if campaign_type == "HighBudgetCampaign":
            reached_followers = int(self.followers * self.engagement_rate * 1.5)
        elif campaign_type == "LowBudgetCampaign":
            reached_followers = int(self.followers * self.engagement_rate * 0.8)
        else:
            raise ValueError("Invalid campaign type.")
        return reached_followers
