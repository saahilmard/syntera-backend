import os
from openai import AsyncOpenAI
from app.schemas import SOAPNote
from app.utils.logger import logger
from config import settings


# Initialize client with organization-level authentication
client = AsyncOpenAI(
    api_key=settings.OPENAI_API_KEY,
    organization=settings.OPENAI_ORG_ID if hasattr(settings, 'OPENAI_ORG_ID') else None
)

SOAP_SYSTEM_PROMPT = """You are a pediatric clinical assistant tasked with generating SOAP notes from visit transcripts.
Extract and organize the information into a structured SOAP format:
- Subjective: Patient's reported symptoms and history
- Objective: Clinical findings and measurements
- Assessment: Diagnosis and clinical assessment
- Plan: Treatment plan and follow-up

Be concise but thorough. Use medical terminology appropriately.
Format your response exactly like this:
S: [subjective content]
O: [objective content]
A: [assessment content]
P: [plan content]"""

POLISH_SYSTEM_PROMPT = """You are a pediatric clinical assistant tasked with creating a polished narrative summary from a SOAP note.
Transform the structured SOAP note into a professional, flowing narrative that captures the key points of the visit.
Maintain all important clinical information while making it more readable."""

async def generate_soap_note(transcript: str, patient_age: int, visit_type: str, provider_notes: str = None) -> SOAPNote:
    user_prompt = f"""Visit Type: {visit_type}
Patient Age: {patient_age} months
Transcript: {transcript}
{f'Provider Notes: {provider_notes}' if provider_notes else ''}

Please generate a SOAP note based on this information."""

    try:
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": SOAP_SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.3
        )

        # Parse the response into SOAP sections
        content = response.choices[0].message.content
        sections = content.split("\n")
        soap_dict = {
            "subjective": "",
            "objective": "",
            "assessment": "",
            "plan": ""
        }
        
        current_section = None
        for line in sections:
            line = line.strip()
            if line.startswith("S:"):
                current_section = "subjective"
                soap_dict[current_section] = line[2:].strip()
            elif line.startswith("O:"):
                current_section = "objective"
                soap_dict[current_section] = line[2:].strip()
            elif line.startswith("A:"):
                current_section = "assessment"
                soap_dict[current_section] = line[2:].strip()
            elif line.startswith("P:"):
                current_section = "plan"
                soap_dict[current_section] = line[2:].strip()
            elif current_section and line:
                soap_dict[current_section] += " " + line

        return SOAPNote(**soap_dict)
    except Exception as e:
        logger.error(f"Error generating SOAP note: {str(e)}")
        raise

async def generate_polished_note(soap_note: SOAPNote) -> str:
    user_prompt = f"""Please create a polished narrative summary from this SOAP note:

Subjective: {soap_note.subjective}
Objective: {soap_note.objective}
Assessment: {soap_note.assessment}
Plan: {soap_note.plan}"""

    try:
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": POLISH_SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.3
        )

        return response.choices[0].message.content.strip()
    except Exception as e:
        logger.error(f"Error generating polished note: {str(e)}")
        raise 