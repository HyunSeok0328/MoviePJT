<template>
<div class="community">
  <table class="rwd-table">
    <tr>
      <th class = "text-center">제목</th>
      <th>작성일</th>
      <th>작성자</th>
    </tr>
    <tr v-for="review in reviews" :key="review.id" class="p-3">
      <td><router-link :to="{name: 'Review', params: {reviewId: `${review.id}`}}"> {{ review.title }} </router-link></td>
      <td>{{ review.created_at }}</td>
      <td>{{ review.user.username }}</td>
    </tr>
  </table>
  <b-button pill  variant="outline-danger" size="sm" @click="moveToCreateReview" class="createBtn d-block">작성</b-button>

</div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Community',
  data: function () {
    return {
      reviews: null,
      user: [],
    }
  },
  methods: {
    setToken: function(){
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getReviews: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/community/review/',
        headers: this.setToken()
      })
        .then(res => {
          this.reviews = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    moveToCreateReview: function(){
      this.$router.push({ name: 'CreateReview' })
    },
    getUser: function(){
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/username/`,
        headers: this.setToken()
      })
        .then((res) => {
          this.user = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },


  },
  created: function () {
    if (localStorage.getItem('jwt')){
      this.getReviews()
      this.getUser()
    } else {
      this.$router.push({ name: 'Login' })
    }
  },
}

</script>

<style scoped>
@import "https://fonts.googleapis.com/css?family=Montserrat:300,400,700";
.rwd-table {
  position: relative;
  margin-top: 5rem;
  margin-right: auto;
  margin-left: auto;
  overflow: hidden;
  width: 55vw;

}
.rwd-table tr {
  border-top: 1px solid #ddd;
  border-bottom: 1px solid #ddd;
}
.rwd-table th {
  display: none;
}
.rwd-table td {
  display: block;
}
.rwd-table td:first-child {
  padding-top: .5em;
}
.rwd-table td:last-child {
  padding-bottom: .5em;
}
.rwd-table td:before {
  content: attr(data-th) ": ";
  font-weight: bold;
  width: 6.5em;
  display: inline-block;
}
@media (min-width: 480px) {
  .rwd-table td:before {
    display: none;
  }
}
.rwd-table th, .rwd-table td {
  text-align: left;
}
@media (min-width: 480px) {
  .rwd-table th, .rwd-table td {
    display: table-cell;
    padding: .25em .5em;
  }
  .rwd-table th:first-child, .rwd-table td:first-child {
    padding-left: 0;
  }
  .rwd-table th:last-child, .rwd-table td:last-child {
    padding-right: 0;
  }
}

body {
  padding: 0 2em;
  font-family: Montserrat, sans-serif;
  -webkit-font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
  color: #444;
  background: #eee;
}

h1 {
  font-weight: normal;
  letter-spacing: -1px;
  color: #34495E;
}

.rwd-table {
  background: #2a2c2f;
  color: #fff;
  border-radius: .4em;
  overflow: hidden;
}
.rwd-table tr {
  border-color: #7a838b;
}
.rwd-table th, .rwd-table td {
  margin: .5em 1em;
}
@media (min-width: 480px) {
  .rwd-table th, .rwd-table td {
    padding: 1em !important;
  }
}
.rwd-table th, .rwd-table td:before {
  color: #CB0707;
}
a {
  text-decoration: none;
  color: white;
}

a:hover {
  color: #f72307;
}

.createBtn {
  margin-top: 40px;
  margin-left: 75vw;
}
</style>