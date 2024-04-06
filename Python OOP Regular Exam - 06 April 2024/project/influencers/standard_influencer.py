from project.influencers.base_influencer import BaseInfluencer
from project.campaigns.base_campaign import BaseCampaign

class StandardInfluencer(BaseInfluencer):
    def __init__(self, username: str, followers: int, engagement_rate: float):
        super().__init__(username, followers, engagement_rate)

    def calculate_payment(self, campaign: BaseCampaign) -> float:
        # Payment calculation based on the campaign's budget and the influencer's payment percentage
        payment = campaign.budget * 0.45
        return payment

    def reached_followers(self, campaign_type: str) -> int:
        # Reached followers calculation based on the campaign type and influencer's attributes
        if campaign_type == "HighBudgetCampaign":
            reached_followers = int(self.followers * self.engagement_rate * 1.2)
        elif campaign_type == "LowBudgetCampaign":
            reached_followers = int(self.followers * self.engagement_rate * 0.9)
        else:
            raise ValueError("Invalid campaign type")

        return reached_followers
