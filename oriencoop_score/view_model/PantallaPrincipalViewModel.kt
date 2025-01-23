package com.example.oriencoop_score.view_model

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.oriencoop_score.repository.UserRepository
import com.example.oriencoop_score.model.UserResponse
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.launch
import com.example.oriencoop_score.Result

class PantallaPrincipalViewModel : ViewModel() {
    private val repository = UserRepository()
    private val _users = MutableStateFlow<Result<List<UserResponse>>?>(null)
    val users: StateFlow<Result<List<UserResponse>>?> = _users

    private val _isLoading = MutableStateFlow(false)
    val isLoading: StateFlow<Boolean> = _isLoading

    fun fetchAllUsers() {
        viewModelScope.launch {
            _isLoading.value = true
            _users.value = Result.Loading
            _users.value = repository.getAllUsers()
            _isLoading.value = false
        }
    }

    /*
    suspend fun onSelected() {
        _isLoading.value = true
        delay(4000) // Simulate a long-running operation
        _isLoading.value = false
    }
     */
}

