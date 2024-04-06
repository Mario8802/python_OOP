from project.influencers.standard_influencer import StandardInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign

class InfluencerManagerApp:
    def __init__(self):
        self.influencers = []
        self.campaigns = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float) -> str:
        if influencer_type not in ("PremiumInfluencer", "StandardInfluencer"):
            return f"{influencer_type} is not an allowed influencer type."

        if any(i.username == username for i in self.influencers):
            return f"{username} is already registered."

        influencer = PremiumInfluencer(username, followers, engagement_rate) if influencer_type == "PremiumInfluencer" else StandardInfluencer(username, followers, engagement_rate)
        self.influencers.append(influencer)
        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float) -> str:
        global campaign
        if campaign_type not in ("HighBudgetCampaign", "LowBudgetCampaign"):
            return f"{campaign_type} is not a valid campaign type."

        if any(campaign.campaign_id == campaign_id for campaign in self.campaigns):
            return f"Campaign ID {campaign_id} has already been created."

        if campaign_type == "LowBudgetCampaign":
            campaign = LowBudgetCampaign(campaign_id, brand, required_engagement)
        elif campaign_type == "HighBudgetCampaign":
            campaign = HighBudgetCampaign(campaign_id, brand, required_engagement)

        self.campaigns.append(campaign)
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int) -> str:
        influencer = next((i for i in self.influencers if i.username == influencer_username), None)
        if influencer is None:
            return f"Influencer '{influencer_username}' not found."

        campaign = next((c for c in self.campaigns if c.campaign_id == campaign_id), None)
        if campaign is None:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility(influencer.engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."

        payment = influencer.calculate_payment(campaign)
        if payment > 0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= payment
            influencer.campaigns_participated.append(campaign)
            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."

        return ""

    def calculate_total_reached_followers(self) -> dict:
        total_followers = {}
        for campaign in self.campaigns:
            if isinstance(campaign, LowBudgetCampaign):
                followers = sum(influencer.reached_followers(campaign) for influencer in campaign.approved_influencers)
                if followers > 0:
                    total_followers[campaign] = followers
        return total_followers

    def influencer_campaign_report(self, username: str) -> str:
        influencer = next((i for i in self.influencers if i.username == username), None)
        if influencer is None:
            return f"{username} has not participated in any campaigns."
        return influencer.display_campaigns_participated()

    def campaign_statistics(self) -> str:
        sorted_campaigns = sorted(self.campaigns, key=lambda c: (len(c.approved_influencers), -c.budget))
        statistics = "$$ Campaign Statistics $$\n"
        for campaign in sorted_campaigns:
            if isinstance(campaign, LowBudgetCampaign):
                followers = self.calculate_total_reached_followers().get(campaign, 0)
                statistics += f"  * Brand: {campaign.brand}, Total influencers: {len(campaign.approved_influencers)}, Total budget: ${campaign.budget:.2f}, Total reached followers: {followers}\n"
        return statistics
