class Net {
    static eval_chord_code(chord_code_string) {
        const url = "http://localhost:5000/eval_chord_code"
        const data = {
            content: chord_code_string,
        }

        fetch(url, {
            method: "POST",
            headers: { 'Content-type': 'application/json' },
            body: JSON.stringify(data)
        }).then(response => {
            if (!response.ok) throw new Error("network skibidied out of sigma... :(")
            return response.json()
        }).then(response_data => {
            console.log("server response: ", response_data)
        }).catch(error => {
            console.error("ayyyy, serverito responsito errorito, errorita serverita", error)
        })
    }
}