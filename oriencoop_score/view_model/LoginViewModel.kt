package com.example.oriencoop_score.view_model

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import kotlinx.coroutines.delay

class LoginViewModel : ViewModel(){
    private val _rut = MutableLiveData<String>()
    val rut : LiveData<String> = _rut

    private val _password = MutableLiveData<String>()
    val password : LiveData<String> = _password

    private val _loginEnable = MutableLiveData<Boolean>()
    val loginEnable : LiveData<Boolean> = _loginEnable

    private val _isLoading = MutableLiveData<Boolean>()
    val isLoading : LiveData<Boolean> = _isLoading

    fun onLoginChanged(rut: String, password: String) {
        _rut.value = rut
        _password.value = password
        _loginEnable.value = isValidPassword(password)


    }
    private fun isValidPassword(password: String): Boolean = password.length >= 6
    /*private fun isValidRut(rut: String): Boolean =*/

    //se usa suspend porque es una corrutina
    suspend fun onLoginSelected(){
        _isLoading.value = true
        delay(4000)
        _isLoading.value = false
    }

}