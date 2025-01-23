package com.example.oriencoop_score.view_model

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.oriencoop_score.model.UserResponse
import com.example.oriencoop_score.model.UserResponseWrapper
import com.example.oriencoop_score.repository.UserRepository
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch
class LoginViewModel : ViewModel() {
    private val repository = UserRepository()

    private val _rut = MutableLiveData<String>()
    val rut: LiveData<String> = _rut

    private val _password = MutableLiveData<String>()
    val password: LiveData<String> = _password

    private val _loginEnable = MutableLiveData<Boolean>()
    val loginEnable: LiveData<Boolean> = _loginEnable

    private val _isLoading = MutableLiveData<Boolean>()
    val isLoading: LiveData<Boolean> = _isLoading

    private val _loginResult = MutableLiveData<com.example.oriencoop_score.Result<UserResponseWrapper>?>() // Fully qualified
    val loginResult: LiveData<com.example.oriencoop_score.Result<UserResponseWrapper>?> = _loginResult

    fun onLoginChanged(rut: String, password: String) {
        _rut.value = rut
        _password.value = password
        //_loginEnable.value = isValidPassword(password) && isValidRut(rut)
    }

    private fun isValidPassword(password: String): Boolean = password.length >= 6

    private fun isValidRut(rut: String): Boolean {
        return rut.isNotEmpty()
    }

    fun onLoginSelected() {
        viewModelScope.launch {
            _isLoading.value = true

            val rut = _rut.value ?: ""
            val password = _password.value ?: ""
            val loginRequest = UserResponse(rut, password)

            val result = repository.validateLogin(loginRequest) // Fully qualified
            _loginResult.value = result

            _isLoading.value = false
        }
    }
}