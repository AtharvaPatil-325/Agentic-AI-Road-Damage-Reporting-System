const severityLevels = [
  { id: 'low', label: 'Low', color: 'green', description: 'Minor damage, not immediately dangerous' },
  { id: 'medium', label: 'Medium', color: 'yellow', description: 'Moderate damage, may cause inconvenience' },
  { id: 'high', label: 'High', color: 'red', description: 'Severe damage, potentially dangerous' }
]

function SeveritySelector({ onSelect, disabled }) {
  return (
    <div className="space-y-3">
      {severityLevels.map((severity) => (
        <button
          key={severity.id}
          onClick={() => onSelect(severity.id)}
          disabled={disabled}
          className={`w-full bg-white border-2 rounded-lg p-4 hover:border-${severity.color}-500 hover:bg-${severity.color}-50 transition-all text-left disabled:opacity-50 disabled:cursor-not-allowed ${
            severity.id === 'low' ? 'border-green-200' :
            severity.id === 'medium' ? 'border-yellow-200' :
            'border-red-200'
          }`}
        >
          <div className="flex items-center justify-between">
            <div>
              <h3 className="font-semibold text-civic-900">{severity.label} Severity</h3>
              <p className="text-sm text-civic-600 mt-1">{severity.description}</p>
            </div>
            <div className={`w-4 h-4 rounded-full bg-${severity.color}-500`}></div>
          </div>
        </button>
      ))}
    </div>
  )
}

export default SeveritySelector


