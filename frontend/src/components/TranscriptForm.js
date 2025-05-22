import React, { useState } from 'react';
import { generateSOAPNote, regeneratePolishedNote } from '../services/api';

const TranscriptForm = () => {
  const [transcript, setTranscript] = useState('');
  const [patientAge, setPatientAge] = useState('');
  const [visitType, setVisitType] = useState('Sick Visit');
  const [providerNotes, setProviderNotes] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      const response = await generateSOAPNote(
        transcript,
        parseInt(patientAge),
        visitType,
        providerNotes
      );
      setResult(response);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleRegenerate = async () => {
    if (!result?.soap_note) return;
    
    setLoading(true);
    setError(null);

    try {
      const response = await regeneratePolishedNote(result.soap_note);
      setResult(prev => ({ ...prev, polished_note: response.polished_note }));
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-2xl mx-auto p-4">
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block text-sm font-medium text-gray-700">Transcript</label>
          <textarea
            value={transcript}
            onChange={(e) => setTranscript(e.target.value)}
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
            rows="4"
            required
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700">Patient Age (months)</label>
          <input
            type="number"
            value={patientAge}
            onChange={(e) => setPatientAge(e.target.value)}
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
            required
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700">Visit Type</label>
          <select
            value={visitType}
            onChange={(e) => setVisitType(e.target.value)}
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
          >
            <option value="Sick Visit">Sick Visit</option>
            <option value="Well Child">Well Child</option>
            <option value="Follow Up">Follow Up</option>
          </select>
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700">Provider Notes (Optional)</label>
          <textarea
            value={providerNotes}
            onChange={(e) => setProviderNotes(e.target.value)}
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
            rows="2"
          />
        </div>

        <button
          type="submit"
          disabled={loading}
          className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
        >
          {loading ? 'Generating...' : 'Generate SOAP Note'}
        </button>
      </form>

      {error && (
        <div className="mt-4 p-4 bg-red-50 text-red-700 rounded-md">
          {error}
        </div>
      )}

      {result && (
        <div className="mt-8 space-y-6">
          <div>
            <h3 className="text-lg font-medium text-gray-900">SOAP Note</h3>
            <div className="mt-2 space-y-4">
              <div>
                <h4 className="font-medium">Subjective</h4>
                <p className="mt-1">{result.soap_note.subjective}</p>
              </div>
              <div>
                <h4 className="font-medium">Objective</h4>
                <p className="mt-1">{result.soap_note.objective}</p>
              </div>
              <div>
                <h4 className="font-medium">Assessment</h4>
                <p className="mt-1">{result.soap_note.assessment}</p>
              </div>
              <div>
                <h4 className="font-medium">Plan</h4>
                <p className="mt-1">{result.soap_note.plan}</p>
              </div>
            </div>
          </div>

          <div>
            <div className="flex justify-between items-center">
              <h3 className="text-lg font-medium text-gray-900">Polished Note</h3>
              <button
                onClick={handleRegenerate}
                disabled={loading}
                className="text-sm text-indigo-600 hover:text-indigo-500"
              >
                Regenerate
              </button>
            </div>
            <p className="mt-2 whitespace-pre-wrap">{result.polished_note}</p>
          </div>
        </div>
      )}
    </div>
  );
};

export default TranscriptForm; 