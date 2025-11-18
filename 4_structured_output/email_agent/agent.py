from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field


# --- Define Output Schema ---
class EmailContent(BaseModel):
    subject: str = Field(
        title="Email Subject",
        description="The subject line of the Email. Should be concise and descriptive."
    )
    body: str = Field(
        title="Email Body",
        description="The main content of the Email. Should be well-formatted with proper greeting, paragraphs and signature"
    )
    
# --- Create Email Generator Agent ---
root_agent = LlmAgent(
    name="email_agent",
    model="gemini-2.0-flash",
    description="Generates professional emails with structured subject and body",
    instruction="""
    You are an Email Generation Assistant.
    Your task is to generate a professional email based on the user's request.
    
    GUIDELINES:
    - Create an appropriate subject line (concise and relevant)
    - Write a well-structured email body with:
        * Professional greeting
        * Clean and concise main content
        * Appropriate closing
        * User name as signature
    - Suggest relevant attachments if applicable (empty list if none is needed)
    - Email tone should match the purpose (formal for business, friendly for colleagues)
    - Keep emails concise but complete
    
    IMPORTANT: Your response MUST be a valid JSON matching this structure:
    {
        "subject": "Subject line here",
        "body": "Email body here with proper paragraphs and formatting",
    }
    
    DO NOT include any explainations or additional text outside the JSON response.
    """,
    output_schema=EmailContent,
    output_key="email",
)

