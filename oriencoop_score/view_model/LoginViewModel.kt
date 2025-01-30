package com.example.oriencoop_score.view_model

import android.util.Log
import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.oriencoop_score.LoginState
import com.example.oriencoop_score.Pantalla
import com.example.oriencoop_score.repository.LoginRepository
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch
import com.example.oriencoop_score.Result
import com.example.oriencoop_score.model.HiddenLoginResponse
import com.example.oriencoop_score.model.UserLoginResponse
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.sync.Mutex

class LoginViewModel : ViewModel() {
    private val loginRepository = LoginRepository()
    private val _loginState = MutableStateFlow<LoginState>(LoginState.Idle)
    private val mutex = Mutex()
    val loginState: StateFlow<LoginState> = _loginState

    fun performLogin(username: String, password: String) {
        viewModelScope.launch {
            viewModelScope.launch {
                if (!mutex.tryLock()) return@launch
            } // Prevent concurrent execution


            _loginState.value = LoginState.Loading
            try {
                // Step 1: Perform Hidden Login with hardcoded credentials
                Log.d("Login", "Performing hidden login...")
                val hiddenLoginResult = loginRepository.performHiddenLogin("admin", "securepassword")
                if (hiddenLoginResult is Result.Success) {
                    val token = hiddenLoginResult.data.token // Extract the token field
                    Log.d("Login", "Hidden login result: $hiddenLoginResult")

                    // Step 2: Perform User Login with user-provided credentials and token
                    Log.d("Login", "Performing user login with token: $token")
                    val userLoginResult = loginRepository.performUserLogin(username, password, token)
                    if (userLoginResult is Result.Success) {
                        _loginState.value = LoginState.Success(userLoginResult.data)
                    } else if (userLoginResult is Result.Error) {
                        _loginState.value = LoginState.Error(
                            userLoginResult.exception.message ?: "User login failed"
                        )
                    }
                } else if (hiddenLoginResult is Result.Error) {
                    _loginState.value = LoginState.Error(
                        hiddenLoginResult.exception.message ?: "Hidden login failed"
                    )
                }
            } catch (e: Exception) {
                _loginState.value = LoginState.Error(e.message ?: "An unexpected error occurred")
            } finally {
                mutex.unlock()
            }
        }
    }
}






/* //VERSION ANTIGUA VIEW MODEL QUE PERMITE LOGEAR CON MAS DE 6 CARACTERES EN LA CONTRASEÑA
    //private val repository = UserRepository()
    private val _rut = MutableLiveData<String>()
    val rut: LiveData<String> = _rut

    private val _password = MutableLiveData<String>()
    val password: LiveData<String> = _password

    private val _loginEnable = MutableLiveData<Boolean>()
    val loginEnable: LiveData<Boolean> = _loginEnable

    private val _isLoading = MutableLiveData<Boolean>()
    val isLoading: LiveData<Boolean> = _isLoading

    fun onLoginChanged(rut: String, password: String) {
        _rut.value = rut
        _password.value = password
        //_loginEnable.value = isValidPassword(password) && isValidRut(rut)
    }

    private fun isValidPassword(password: String): Boolean = password.length >= 6

    private fun isValidRut(rut: String): Boolean {
        return rut.isNotEmpty()
    }

    fun onLoginSelected() {/*
        viewModelScope.launch {
            _isLoading.value = true

            val rut = _rut.value ?: ""
            val password = _password.value ?: ""
            val loginRequest = UserResponse(rut, password)

            val result = repository.validateLogin(loginRequest) // Fully qualified
            _loginResult.value = result

            _isLoading.value = false
        }*/
    }*/