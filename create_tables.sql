-- Copy of Users table
CREATE TABLE CW2.Users (
    user_id INT PRIMARY KEY,
    name NVARCHAR(100) NOT NULL,
    email NVARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE CW2.Roles (
    role_id INT PRIMARY KEY,
    role_name NVARCHAR(50) NOT NULL
);

CREATE TABLE CW2.UserRoles (
    user_role_id INT PRIMARY KEY IDENTITY(1,1),
    user_id INT FOREIGN KEY REFERENCES CW2.Users(user_id),
    role_id INT FOREIGN KEY REFERENCES CW2.Roles(role_id)
);

CREATE TABLE CW2.Trails (
    trail_id INT PRIMARY KEY,
    name NVARCHAR(200) NOT NULL,
    location NVARCHAR(200) NOT NULL
);

CREATE TABLE CW2.Comments (
    comment_id INT PRIMARY KEY IDENTITY(1,1),
    trail_id INT FOREIGN KEY REFERENCES CW2.Trails(trail_id),
    user_id INT FOREIGN KEY REFERENCES CW2.Users(user_id),
    comment_text NVARCHAR(MAX) NOT NULL,
    created_at DATETIME DEFAULT GETDATE(),
    updated_at DATETIME NULL,
    is_archived BIT DEFAULT 0
);

CREATE TABLE CW2.CommentLogs (
    log_id INT PRIMARY KEY IDENTITY(1,1),
    comment_id INT FOREIGN KEY REFERENCES CW2.Comments(comment_id),
    action NVARCHAR(50),
    action_time DATETIME DEFAULT GETDATE()
);