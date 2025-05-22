const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api/v1';

export const generateSOAPNote = async (transcript, patientAge, visitType, providerNotes = '') => {
  try {
    const response = await fetch(`${API_BASE_URL}/generate_note`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        transcript,
        patient_age: patientAge,
        visit_type: visitType,
        provider_notes: providerNotes,
      }),
    });

    if (!response.ok) {
      throw new Error('Failed to generate SOAP note');
    }

    return await response.json();
  } catch (error) {
    console.error('Error generating SOAP note:', error);
    throw error;
  }
};

export const regeneratePolishedNote = async (soapNote) => {
  try {
    const response = await fetch(`${API_BASE_URL}/regenerate`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        soap_note: soapNote,
      }),
    });

    if (!response.ok) {
      throw new Error('Failed to regenerate polished note');
    }

    return await response.json();
  } catch (error) {
    console.error('Error regenerating polished note:', error);
    throw error;
  }
}; 