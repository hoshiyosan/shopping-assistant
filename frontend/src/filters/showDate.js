import Vue from 'vue'

Vue.filter('showDate', function (datetimeString) {
    const date = new Date(datetimeString);
    return `${date.toLocaleDateString('fr-FR')} ${date.toLocaleTimeString('fr-FR')}`
})
