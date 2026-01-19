import React, { createContext, useContext, useState, useCallback } from 'react';
import { CheckCircle2, AlertCircle, Info, X } from 'lucide-react';

const ToastContext = createContext();

export const ToastProvider = ({ children }) => {
  const [toasts, setToasts] = useState([]);

  const showToast = useCallback((message, type = 'success') => {
    const id = Date.now();
    setToasts((prev) => [...prev, { id, message, type }]);
    setTimeout(() => {
      removeToast(id);
    }, 4000);
  }, []);

  const removeToast = useCallback((id) => {
    setToasts((prev) => prev.filter((t) => t.id !== id));
  }, []);

  return (
    <ToastContext.Provider value={{ showToast }}>
      {children}
      <div className="fixed bottom-24 left-1/2 -translate-x-1/2 z-[100] flex flex-col items-center space-y-3 w-full max-w-xs pointer-events-none">
        {toasts.map((toast) => (
          <div 
            key={toast.id} 
            className="pointer-events-auto glass-premium flex items-center space-x-3 p-4 pr-6 rounded-2xl border-white/10 shadow-2xl animate-in slide-in-from-bottom-4 duration-300"
          >
            <div className={`
              w-8 h-8 rounded-xl flex items-center justify-center
              ${toast.type === 'success' ? 'bg-emerald-500/20 text-emerald-400' : 
                toast.type === 'error' ? 'bg-red-500/20 text-red-500' : 
                'bg-blue-500/20 text-blue-400'}
            `}>
              {toast.type === 'success' ? <CheckCircle2 size={18} /> : 
               toast.type === 'error' ? <AlertCircle size={18} /> : 
               <Info size={18} />}
            </div>
            <p className="text-sm font-bold tracking-tight text-white">{toast.message}</p>
            <button onClick={() => removeToast(toast.id)} className="text-slate-500 hover:text-white transition-colors">
              <X size={14} />
            </button>
          </div>
        ))}
      </div>
    </ToastContext.Provider>
  );
};

export const useToast = () => useContext(ToastContext);
