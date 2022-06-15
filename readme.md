## JOKER-BOT

A reddit bot using python3 (praw) and sqlite3.  The purpose of this application is to automatically scrape joke-related subreddits for the hottest humorous content and store all resulting jokes in a hilarious database.  The application is currently run on a cron-job every hour in an attempt to retrieve new material--because of this, and because joke subreddits are notorious for reposted material, we expect to find a lot of duplicate data in the tables.

We have begun to address this problem by implementing some database-cleaning functionality that is engineered to minimize the duplication of data.  Thus we aim to create a repository of humor that doesn't suffer from boring old reposts.

Later on, we will develop a frontend component using React and NodeJS in order to display the jokes in a more user-friendly fashion.  We may also implement some sort of search functionality, so a user can find jokes related to a particular subject matter.

Eventually, the app may be containerized using docker/podman in order to wrap up the dependencies into a tidy unit.  Right now, it isn't completely messy, but by the time front end services and routing middlewares are introduced it could become quite challenging to keep it all together.