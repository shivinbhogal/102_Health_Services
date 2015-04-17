
$('#speciality').typeahead({
        source: speciality_list
    });

$('#area').typeahead({
        source: [
            { id: 1, name: 'Pink Square' },
            { id: 2, name: 'Ajmeri Gate' },
        ]
    });

$('#doctor').typeahead({
    source: doc_list
});