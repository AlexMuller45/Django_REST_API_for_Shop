var mix = {
    methods: {
        getSales() {
            this.getData("/api/sales").then(data => {
                this.salesCards = data.salesCards
            })
        },
    },
    mounted() {
        this.getSales();
    },
    data() {
        return {
            salesCards: [],
            // TODO добавить пагинацию
        }
    },
}