#PROJECT TITLE:RECIPE BOOK
A personal recipe book where you can save recipes. Each recipe will have a title, a list of ingredients, and instruction

#####
Core User Features 🧑‍🍳
####
Add a New Recipe: A simple and intuitive form allows you to add new recipes with a title, list of ingredients, step-by-step instructions, and a cuisine type.

View All Recipes: Browse your entire collection of recipes in a clean, organized list. Each recipe can be expanded to see the full details without cluttering the page.

Powerful Ingredient Search: Instantly find a recipe by searching for a single ingredient. This helps you quickly find what you can make with the items you have on hand.
### Project Structure

RECIPE BOOK/
|
|---src/          #core application logic
|   |---logic.py  #Business logic and task
operations
|  |__db.py       #Database operations
|
|----api/         #Backend API
|    |__main.py   #FastAPI endpoints
|
|----frontend/    #Frontend application
|     |__app.py   #Streamlit web interface
|
|___requirements.txt  #Python Dependencies
|
|___README.md   #Project documentation
|
|____.env      #Python Variables

## Quick Start

### Prerequisites

- Python 3.8  or higher
- A Supabase account
- Git(Push,cloning)
  
### 1.Clone or Download the Project
# Option 1: Clone with Git
git clone <repository-url>

# Option 2: Download and extract the Zip file

### 2.Install Dependencies

# Install all required Python packages
pip install -r requirements.txt

### 3. Set Up Supabase Database

1.Create a Supabase Project:

2.Create the Tasks Table:
 
  -Go to the SQL Editor in your Supabase
  dashboard
  -Run this SQL command:

  CREATE TABLE recipe(
       id BIGSERIAL PRIMARY KEY,
       title TEXT NOT NULL,
       ingredients TEXT,
       instructions TEXT NOT NULL,
       due_date date
  );

   ## 4. Configure Environment variables
   1.create a '.env' file in the project root
   2.Add your Supabase credentials to '.env';
   SUPABASE_URL=url = "https://ztudyiaermiounhoejer.supabase.co"
   SUPABASE_KEY= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inp0dWR5aWFlcm1pb3VuaG9lamVyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTgwODM2NTUsImV4cCI6MjA3MzY1OTY1NX0.bB62E2PGORgVnnh6Iar7TtTavYs8JpHJGpLPx_p59gw"
   ### 5.Run the Application

   ### Streamlit frontend
   streamlit run frontend/app.py
   the app will open in your browser at'http://localhost:8501'
   ## FastAPI  Backend
      cd api
      python main.py

  ### How to use

  ## Technical Details

  ## Technologies Used
    - **Frontend** -Streamlit(Python web framework)
    -**Backend**-FastAPI(Python Rest API)
    -**Database**-Supabase(PostgreSQL-based backend-as-a-service)
    -**Language**:Python 3.8+
### Key Components
 1.**'src/db.py'**:Database operations
    -Handles all CRUD operations with Supabase
  2.**'src/logic.py'**: Business logic 
  -Task validation and processing
  ## Future Enhancements
  Ideas for exxtending this project:
-**User Authentication**:Aff user accounts and login
-**Task Categories**:Organize 
## Support