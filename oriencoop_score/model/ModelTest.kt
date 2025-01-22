package com.example.oriencoop_score.model

import java.util.Objects

data class UserResponseWrapper(
        val data: List<UserResponse>
)

data class UserResponse(
        val rut: String,
        val password: Int
)

data class CharactersItem(
        val actor: String,
        val alive: Boolean,
        val alternate_actors: List<String>,
        val alternate_names: List<String>,
        val ancestry: String,
        val dateOfBirth: String,
        val eyeColour: String,
        val gender: String,
        val hairColour: String,
        val hogwartsStaff: Boolean,
        val hogwartsStudent: Boolean,
        val house: String,
        val id: String,
        val image: String,
        val name: String,
        val patronus: String,
        val species: String,
        val wand: Any,
        val wizard: Boolean,
        val yearOfBirth: Int
)