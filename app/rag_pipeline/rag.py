from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from app.rag_pipeline.query_rag_context import get_relevant_context
import os

model = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), temperature=0.3, model="gpt-4")

def generate_soap_notes(transcription, patient_age, visit_type):
    clinical_query = f"pediatric visit type: {visit_type}, age: {patient_age}, symptoms: {transcription}"
    context = get_relevant_context(clinical_query)

    prompt_template = ChatPromptTemplate.from_template("""
    You're a pediatric clinical assistant generating SOAP notes.
    Patient age: {age}, Visit type: {visit}, Clinical transcription: {transcription}

    Use the context below:
    {context}

    Format your response in SOAP format.
    """)

    prompt = prompt_template.format_messages(
        age=patient_age,
        visit=visit_type,
        transcription=transcription,
        context=context
    )

    response = model.invoke(prompt)
    return response.content 