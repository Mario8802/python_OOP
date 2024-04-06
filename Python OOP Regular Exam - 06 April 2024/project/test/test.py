import unittest
from project.social_media import SocialMedia

class TestSocialMedia(unittest.TestCase):
    def setUp(self):
        self.social_media = SocialMedia("testuser", "Instagram", 1000, "Photo")

    def test_correct_init(self):
        self.assertEqual("testuser", self.social_media._username)
        self.assertEqual("Instagram", self.social_media._platform)
        self.assertEqual(1000, self.social_media._followers)
        self.assertEqual("Photo", self.social_media._content_type)
        self.assertEqual([], self.social_media._posts)

    def test_set_invalid_platform_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.social_media.platform = "Facebook"
        self.assertEqual(
            "Platform should be one of ['Instagram', 'YouTube', 'Twitter']",
            str(ve.exception)
        )

    def test_set_negative_followers_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.social_media.followers = -100
        self.assertEqual(
            "Followers cannot be negative.",
            str(ve.exception)
        )

    def test_create_post(self):
        # Test creating a new post
        self.assertEqual(
            self.social_media.create_post("Test post"),
            "New Photo post created by testuser on Instagram."
        )
        # Check if the post is added to the list of posts
        self.assertEqual(len(self.social_media._posts), 1)
        self.assertEqual(self.social_media._posts[0]['content'], "Test post")

    def test_like_post(self):
        # Test liking a post
        self.social_media.create_post("Test post")
        self.assertEqual(
            self.social_media.like_post(0),
            "Post liked by testuser."
        )
        # Check if the post's likes are incremented
        self.assertEqual(self.social_media._posts[0]['likes'], 1)

    def test_like_post_max_likes(self):
        # Test liking a post that has reached the maximum number of likes
        self.social_media.create_post("Test post")
        # Like the post 10 times
        for _ in range(10):
            self.social_media.like_post(0)
        # The 11th like should fail
        self.assertEqual(
            self.social_media.like_post(0),
            "Post has reached the maximum number of likes."
        )
        # Check if the likes are capped at 10
        self.assertEqual(self.social_media._posts[0]['likes'], 10)

    def test_comment_on_post(self):
        # Test commenting on a post
        self.social_media.create_post("Test post")
        self.assertEqual(
            self.social_media.comment_on_post(0, "This is a nice post!"),
            "Comment added by testuser on the post."
        )
        # Check if the comment is added to the post
        self.assertEqual(len(self.social_media._posts[0]['comments']), 1)
        self.assertEqual(self.social_media._posts[0]['comments'][0]['comment'], "This is a nice post!")

    def test_comment_on_post_short_comment(self):
        # Test commenting on a post with a comment less than 10 characters
        self.social_media.create_post("Test post")
        self.assertEqual(
            self.social_media.comment_on_post(0, "Short"),
            "Comment should be more than 10 characters."
        )
        # Check if the comment is not added due to its length
        self.assertEqual(len(self.social_media._posts[0]['comments']), 0)

    def test_comment_on_post_invalid_index(self):
        # Test commenting on a post with an invalid index
        # Create a post to ensure there is at least one post available
        self.social_media.create_post("Test post")

        # Attempt to comment on a post with index 1, which should be invalid
        with self.assertRaises(IndexError):
            self.social_media.comment_on_post(1, "This is a nice post!")

    def test_create_post_with_invalid_platform(self):
        # Test creating a post with an invalid platform
        with self.assertRaises(ValueError):
            self.social_media = SocialMedia("testuser", "Facebook", 1000, "Photo")

    def test_create_post_with_negative_followers(self):
        # Test creating a post with negative followers
        with self.assertRaises(ValueError):
            self.social_media = SocialMedia("testuser", "Instagram", -100, "Photo")

    def test_create_post_with_invalid_content_type(self):
        # Test creating a post with an invalid content type
        with self.assertRaises(ValueError):
            self.social_media = SocialMedia("testuser", "Instagram", 1000, "Video")

    def test_like_post_with_invalid_index(self):
        # Test liking a post with an invalid index
        self.social_media.create_post("Test post")
        with self.assertRaises(IndexError):
            self.social_media.like_post(1)

    def test_like_post_reaches_maximum_likes(self):
        # Test liking a post that has reached the maximum number of likes
        self.social_media.create_post("Test post")
        for _ in range(10):
            self.social_media.like_post(0)
        self.assertEqual(self.social_media.like_post(0), "Post has reached the maximum number of likes.")

    def test_comment_on_post_reaches_maximum_comments(self):
        # Test commenting on a post with maximum comments
        self.social_media.create_post("Test post")
        for _ in range(10):
            self.social_media.comment_on_post(0, "This is a nice post!")
        self.assertEqual(self.social_media.comment_on_post(0, "This is a nice post!"), "Maximum comments reached.")


if __name__ == '__main__':
    unittest.main()
