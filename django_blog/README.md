# Blog Post Management (CRUD)

This app allows:
- Viewing all posts (/posts/)
- Viewing a single post (/posts/<id>/)
- Creating a new post (/posts/new/) [login required]
- Editing a post (/posts/<id>/edit/) [author only]
- Deleting a post (/posts/<id>/delete/) [author only]

Permissions:
- Authenticated users can create posts.
- Only the post author can edit or delete.
- Public can view posts.
