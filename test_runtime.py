"""
Tests for WASM-SDK-CORE-PY Runtime
"""

import pytest
from wasm_sdk_core import Runtime, RuntimeConfig, init, version


class TestVersion:
    """Test version information"""
    
    def test_version_exists(self):
        """Test that version string exists"""
        ver = version()
        assert ver is not None
        assert isinstance(ver, str)
        assert len(ver) > 0
    
    def test_version_format(self):
        """Test version string format"""
        ver = version()
        parts = ver.split('.')
        assert len(parts) == 3
        assert all(part.isdigit() for part in parts)


class TestInit:
    """Test init function"""
    
    def test_init_returns_runtime(self):
        """Test that init returns a Runtime instance"""
        runtime = init()
        assert isinstance(runtime, Runtime)
        assert runtime.is_initialized()
    
    def test_init_default_config(self):
        """Test that init creates runtime with default configuration"""
        runtime = init()
        assert runtime.is_pyo3_enabled()
        assert runtime.is_boa_enabled()


class TestRuntimeConfig:
    """Test RuntimeConfig class"""
    
    def test_default_config(self):
        """Test default configuration values"""
        config = RuntimeConfig()
        assert config.pyo3_enabled is True
        assert config.boa_enabled is True
        assert config.max_memory == 1024 * 1024 * 1024
        assert config.wasm_support is True
    
    def test_custom_config(self):
        """Test custom configuration values"""
        config = RuntimeConfig(
            pyo3_enabled=False,
            boa_enabled=False,
            max_memory=512 * 1024 * 1024,
            wasm_support=False
        )
        assert config.pyo3_enabled is False
        assert config.boa_enabled is False
        assert config.max_memory == 512 * 1024 * 1024
        assert config.wasm_support is False
    
    def test_partial_config(self):
        """Test partial configuration with defaults"""
        config = RuntimeConfig(max_memory=256 * 1024 * 1024)
        assert config.pyo3_enabled is True  # default
        assert config.max_memory == 256 * 1024 * 1024
    
    def test_config_repr(self):
        """Test configuration string representation"""
        config = RuntimeConfig()
        repr_str = repr(config)
        assert "RuntimeConfig" in repr_str
        assert "pyo3_enabled" in repr_str


class TestRuntime:
    """Test Runtime class"""
    
    def test_runtime_creation_default(self):
        """Test runtime creation with default config"""
        runtime = Runtime()
        assert runtime.is_initialized()
        assert runtime.is_pyo3_enabled()
        assert runtime.is_boa_enabled()
    
    def test_runtime_creation_custom_config(self):
        """Test runtime creation with custom config"""
        config = RuntimeConfig(max_memory=512 * 1024 * 1024)
        runtime = Runtime(config)
        assert runtime.get_config().max_memory == 512 * 1024 * 1024
    
    def test_is_pyo3_enabled(self):
        """Test pyo3 enabled check"""
        runtime = Runtime()
        assert runtime.is_pyo3_enabled() is True
        
        config = RuntimeConfig(pyo3_enabled=False)
        runtime_disabled = Runtime(config)
        assert runtime_disabled.is_pyo3_enabled() is False
    
    def test_is_boa_enabled(self):
        """Test Boa enabled check"""
        runtime = Runtime()
        assert runtime.is_boa_enabled() is True
        
        config = RuntimeConfig(boa_enabled=False)
        runtime_disabled = Runtime(config)
        assert runtime_disabled.is_boa_enabled() is False
    
    def test_is_initialized(self):
        """Test initialization check"""
        runtime = Runtime()
        assert runtime.is_initialized() is True
    
    def test_execute_python(self):
        """Test Python code execution"""
        runtime = Runtime()
        result = runtime.execute_python("2 + 2")
        assert result == 4
    
    def test_execute_python_disabled(self):
        """Test Python execution when pyo3 is disabled"""
        config = RuntimeConfig(pyo3_enabled=False)
        runtime = Runtime(config)
        with pytest.raises(RuntimeError, match="pyo3 is not enabled"):
            runtime.execute_python("2 + 2")
    
    def test_execute_python_complex(self):
        """Test complex Python code execution"""
        runtime = Runtime()
        result = runtime.execute_python("[1, 2, 3, 4, 5]")
        assert result == [1, 2, 3, 4, 5]
    
    def test_execute_javascript(self):
        """Test JavaScript code execution"""
        runtime = Runtime()
        result = runtime.execute_javascript("console.log('test')")
        assert isinstance(result, str)
        assert "test" in result
    
    def test_execute_javascript_disabled(self):
        """Test JavaScript execution when Boa is disabled"""
        config = RuntimeConfig(boa_enabled=False)
        runtime = Runtime(config)
        with pytest.raises(RuntimeError, match="Boa engine is not enabled"):
            runtime.execute_javascript("test")
    
    def test_pyo3_version(self):
        """Test pyo3 version retrieval"""
        runtime = Runtime()
        ver = runtime.pyo3_version()
        assert isinstance(ver, str)
        assert len(ver) > 0
    
    def test_boa_version(self):
        """Test Boa version retrieval"""
        runtime = Runtime()
        ver = runtime.boa_version()
        assert isinstance(ver, str)
        assert len(ver) > 0
    
    def test_get_config(self):
        """Test configuration retrieval"""
        config = RuntimeConfig(max_memory=256 * 1024 * 1024)
        runtime = Runtime(config)
        retrieved_config = runtime.get_config()
        assert isinstance(retrieved_config, RuntimeConfig)
        assert retrieved_config.max_memory == 256 * 1024 * 1024
    
    def test_runtime_repr(self):
        """Test runtime string representation"""
        runtime = Runtime()
        repr_str = repr(runtime)
        assert "Runtime" in repr_str
        assert "initialized" in repr_str


class TestMultipleInstances:
    """Test multiple runtime instances"""
    
    def test_independent_instances(self):
        """Test that multiple instances are independent"""
        runtime1 = Runtime(RuntimeConfig(max_memory=512 * 1024 * 1024))
        runtime2 = Runtime(RuntimeConfig(max_memory=256 * 1024 * 1024))
        
        assert runtime1.get_config().max_memory == 512 * 1024 * 1024
        assert runtime2.get_config().max_memory == 256 * 1024 * 1024
    
    def test_independent_states(self):
        """Test that instances maintain independent states"""
        runtime1 = Runtime(RuntimeConfig(pyo3_enabled=True))
        runtime2 = Runtime(RuntimeConfig(pyo3_enabled=False))
        
        assert runtime1.is_pyo3_enabled() is True
        assert runtime2.is_pyo3_enabled() is False


class TestIntegration:
    """Integration tests"""
    
    def test_full_workflow(self):
        """Test complete workflow from init to execution"""
        # Initialize
        runtime = init()
        assert runtime.is_initialized()
        
        # Execute Python
        py_result = runtime.execute_python("10 * 5")
        assert py_result == 50
        
        # Execute JavaScript
        js_result = runtime.execute_javascript("Math.sqrt(16)")
        assert isinstance(js_result, str)
        
        # Get versions
        assert runtime.pyo3_version()
        assert runtime.boa_version()
    
    def test_custom_workflow(self):
        """Test workflow with custom configuration"""
        config = RuntimeConfig(
            pyo3_enabled=True,
            boa_enabled=True,
            max_memory=128 * 1024 * 1024,
            wasm_support=True
        )
        runtime = Runtime(config)
        
        assert runtime.is_initialized()
        assert runtime.get_config().max_memory == 128 * 1024 * 1024
        
        result = runtime.execute_python("'hello'.upper()")
        assert result == "HELLO"
