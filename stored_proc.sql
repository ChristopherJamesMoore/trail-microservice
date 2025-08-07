-- CREATE
IF OBJECT_ID('CW2.AddComment', 'P') IS NOT NULL
    DROP PROCEDURE CW2.AddComment;
GO
CREATE PROCEDURE CW2.AddComment
    @trail_id INT,
    @user_id INT,
    @comment_text NVARCHAR(MAX)
AS
BEGIN
    INSERT INTO CW2.Comments (trail_id, user_id, comment_text)
    VALUES (@trail_id, @user_id, @comment_text);
END;
GO

-- READ
IF OBJECT_ID('CW2.GetComments', 'P') IS NOT NULL
    DROP PROCEDURE CW2.GetComments;
GO
CREATE PROCEDURE CW2.GetComments
AS
BEGIN
    SELECT c.comment_id, c.comment_text, c.created_at, u.name AS user_name, t.name AS trail_name
    FROM CW2.Comments c
    JOIN CW2.Users u ON c.user_id = u.user_id
    JOIN CW2.Trails t ON c.trail_id = t.trail_id
    WHERE c.is_archived = 0;
END;
GO

-- UPDATE
IF OBJECT_ID('CW2.UpdateComment', 'P') IS NOT NULL
    DROP PROCEDURE CW2.UpdateComment;
GO
CREATE PROCEDURE CW2.UpdateComment
    @comment_id INT,
    @user_id INT,
    @comment_text NVARCHAR(MAX)
AS
BEGIN
    UPDATE CW2.Comments
    SET comment_text = @comment_text,
        updated_at = GETDATE()
    WHERE comment_id = @comment_id
      AND user_id = @user_id
      AND is_archived = 0;
END;
GO

-- DELETE (admin)
IF OBJECT_ID('CW2.ArchiveComment', 'P') IS NOT NULL
    DROP PROCEDURE CW2.ArchiveComment;
GO
CREATE PROCEDURE CW2.ArchiveComment
    @comment_id INT
AS
BEGIN
    UPDATE CW2.Comments
    SET is_archived = 1
    WHERE comment_id = @comment_id;
END;
GO
