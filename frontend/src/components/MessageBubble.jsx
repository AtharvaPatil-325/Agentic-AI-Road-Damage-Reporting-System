function MessageBubble({ message }) {
  const isUser = message.role === 'user'
  
  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'} mb-4`}>
      <div className={`chat-message ${isUser ? 'chat-user' : 'chat-assistant'}`}>
        {message.image && (
          <img 
            src={message.image} 
            alt="Uploaded damage" 
            className="w-64 h-48 object-cover rounded-lg mb-2"
          />
        )}
        {message.isLoading ? (
          <div className="flex items-center space-x-2">
            <div className="animate-spin rounded-full h-4 w-4 border-2 border-current border-t-transparent"></div>
            <span>{message.content}</span>
          </div>
        ) : (
          <p className="whitespace-pre-wrap">{message.content}</p>
        )}
        <span className="text-xs opacity-70 mt-1 block">
          {new Date(message.timestamp).toLocaleTimeString()}
        </span>
      </div>
    </div>
  )
}

export default MessageBubble


