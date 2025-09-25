# db_manager.py
import os
from supabase import create_client
from dotenv import load_dotenv

# load environment variables
load_dotenv()
url=os.getenv("SUPABASE_URL")
key=os.getenv("SUPABASE_KEY")
supabase=create_client(url,key)

# Create Task
def create_task(title,ingredients,instructions,due_date):
    return supabase.table("recipe").insert({
        "title":title,
         "ingredients":ingredients,
         "instructions":instructions,
         "due_date":due_date
    }).execute()
#Get All tasks
def get_all_tasks():
    return supabase.table("recipe").select("*").order("due_date").execute

#Update task status
def update_task(task_id,completed):
    return supabase.table("recipe").update({"title":title}).eq("id",task_id).execute()

#Delte Task
def delete_task(task_id):
    return supabase.table("recipe").delete().eq("id",task_id).execute()
create_task("Aloo fry","potato salt onion oil","cook potatoes","2025-10-21") 
# Assuming your function is now called create_recipe() or similar
create_task(
    "Chicken Tikka Masala",
    "Chicken, yogurt, ginger, garlic paste, garam masala, turmeric, tomato puree, cream, onion",
    "1. Marinate chicken in yogurt and spices for at least 1 hour. 2. Grill or pan-fry the chicken until cooked. 3. Make a sauce with onion, tomato puree, and cream. 4. Add chicken to the sauce and simmer for 10 minutes.",
    "2025-09-30"
)                         