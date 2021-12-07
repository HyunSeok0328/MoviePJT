import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies: [],
    // user: [],
  },
  mutations: {
    LOAD_MOVIE: function (state, results) {
      state.movies = results
    },
    // LOAD_USER: function (state, results) {
    //   state.user = results
    // },
  },
  actions: {
    LoadMovieCards: function ({commit}) {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/home/',
      })
        .then((res) => {
          commit('LOAD_MOVIE', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },

  },
  modules: {
  },
})

