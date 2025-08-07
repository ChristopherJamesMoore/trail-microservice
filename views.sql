CREATE VIEW CW2.ViewComments AS
SELECT c.comment_id, c.comment_text, c.created_at, u.name AS user_name, t.name AS trail_name
FROM CW2.Comments c
JOIN CW2.Users u ON c.user_id = u.user_id
JOIN CW2.Trails t ON c.trail_id = t.trail_id
WHERE c.is_archived = 0;