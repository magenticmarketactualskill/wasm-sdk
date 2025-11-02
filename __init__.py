"""
WASM-SDK-CORE-PY

Python bindings for WASM SDK Core using pyo3 and Boa engine.
Provides runtime for executing Python and JavaScript code with WebAssembly support.
"""

from typing import Any, Optional

try:
    from ._core import Runtime, RuntimeConfig, init, version
except ImportError:
    # Fallback for development without compiled extension
    import warnings
    warnings.warn(
        "Native extension not found. Using pure Python fallback. "
        "Run 'maturin develop' to build the extension.",
        ImportWarning
    )
    
    class RuntimeConfig:
        """Runtime configuration for WASM-SDK-CORE-PY"""
        
        def __init__(
            self,
            pyo3_enabled: bool = True,
            boa_enabled: bool = True,
            max_memory: int = 1024 * 1024 * 1024,
            wasm_support: bool = True
        ):
            self.pyo3_enabled = pyo3_enabled
            self.boa_enabled = boa_enabled
            self.max_memory = max_memory
            self.wasm_support = wasm_support
        
        def __repr__(self) -> str:
            return (
                f"RuntimeConfig(pyo3_enabled={self.pyo3_enabled}, "
                f"boa_enabled={self.boa_enabled}, max_memory={self.max_memory}, "
                f"wasm_support={self.wasm_support})"
            )
    
    class Runtime:
        """Main runtime class for executing Python and JavaScript"""
        
        def __init__(self, config: Optional[RuntimeConfig] = None):
            self.config = config or RuntimeConfig()
            self.initialized = True
            self._pyo3_version = "0.22.0"
            self._boa_version = "0.19.0"
        
        def is_pyo3_enabled(self) -> bool:
            """Check if pyo3 is enabled"""
            return self.config.pyo3_enabled
        
        def is_boa_enabled(self) -> bool:
            """Check if Boa engine is enabled"""
            return self.config.boa_enabled
        
        def is_initialized(self) -> bool:
            """Check if runtime is initialized"""
            return self.initialized
        
        def execute_python(self, code: str) -> Any:
            """Execute Python code"""
            if not self.initialized:
                raise RuntimeError("Runtime not initialized")
            if not self.config.pyo3_enabled:
                raise RuntimeError("pyo3 is not enabled")
            return eval(code)
        
        def execute_javascript(self, code: str) -> str:
            """Execute JavaScript code (simulated)"""
            if not self.initialized:
                raise RuntimeError("Runtime not initialized")
            if not self.config.boa_enabled:
                raise RuntimeError("Boa engine is not enabled")
            return f"JavaScript execution simulated: {code}"
        
        def pyo3_version(self) -> str:
            """Get pyo3 version"""
            return self._pyo3_version
        
        def boa_version(self) -> str:
            """Get Boa version"""
            return self._boa_version
        
        def get_config(self) -> RuntimeConfig:
            """Get runtime configuration"""
            return self.config
        
        def __repr__(self) -> str:
            return (
                f"Runtime(initialized={self.initialized}, "
                f"pyo3_enabled={self.config.pyo3_enabled}, "
                f"boa_enabled={self.config.boa_enabled})"
            )
    
    def init() -> Runtime:
        """Initialize runtime with default configuration"""
        return Runtime()
    
    def version() -> str:
        """Get library version"""
        return "0.1.0"


__version__ = version()
__all__ = ["Runtime", "RuntimeConfig", "init", "version"]
