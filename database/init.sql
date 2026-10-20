CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO tasks (title, completed)
VALUES
    ('Learn Docker', FALSE),
    ('Build 3-Tier Application', FALSE),
    ('Deploy on Docker Hub', FALSE);
