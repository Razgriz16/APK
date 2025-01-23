package com.example.oriencoop_score.view_model

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.oriencoop_score.model.CharactersItem
import com.example.oriencoop_score.repository.HarryPotterRepository
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.launch

class HarryPotterViewModel() : ViewModel() {
    private val repository = HarryPotterRepository()
    private val _characters = MutableStateFlow<List<CharactersItem>>(emptyList())
    val characters: StateFlow<List<CharactersItem>> get() = _characters


    fun fetchCharacters() {
        viewModelScope.launch {
            try {
                val characters = repository.getCharacters() // Calls the suspend function
                _characters.value = characters
            } catch (e: Exception) {
                // Handle errors (e.g., show an error message)
                println("Error fetching characters: ${e.message}")
            }
        }
    }


}