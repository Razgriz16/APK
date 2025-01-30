import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.oriencoop_score.repository.MindicatorsRepository
import kotlinx.coroutines.launch
import com.example.oriencoop_score.Result
import com.example.oriencoop_score.model.Indicador

class MindicatorsViewModel(private val repository: MindicatorsRepository) : ViewModel() {

    private val _indicadores = MutableLiveData<Result<Indicador>>()
    val indicadores: LiveData<Result<Indicador>> = _indicadores

    private val _isLoading = MutableLiveData(false)
    val isLoading: LiveData<Boolean> = _isLoading

    init {
        fetchIndicadores()
    }

    fun fetchIndicadores() {
        viewModelScope.launch {
            _isLoading.value = true
            _indicadores.value = repository.getIndicadores()
            _isLoading.value = false
        }
    }

    // Optional: Helper functions to access data in a more convenient way
    fun getUF(): String? {
        return (_indicadores.value as? Result.Success)?.data?.UF
    }

    fun getDolar(): String? {
        return (_indicadores.value as? Result.Success)?.data?.Dolar
    }

    fun getEuro(): String? {
        return (_indicadores.value as? Result.Success)?.data?.Euro
    }

    fun getUTM(): String? {
        return (_indicadores.value as? Result.Success)?.data?.UTM
    }
}