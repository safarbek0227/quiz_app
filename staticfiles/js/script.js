$('.submit').click(function() {
    arr = []
        var radio = $("input[type=radio]").filter(":checked");
        var quiz = $('li.quiz')
        if (radio.length >0) {
            for (const element of radio) {
                arr.push(parseInt(element.id))
                }
        }
        else {
            alert('Nothing is selected');
        }
        $.ajax({
            type: 'GET',
            url: '/check/',
            data: {'data': JSON.stringify(arr),
                   'length': quiz.length},
        });
        window.location.replace("/congratulate/")
    })

