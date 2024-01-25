function addMoreInputPairs() {
    // Clone the template input-container element
    var templateInputContainer = document.querySelector('.input-container');
    var newInputContainer = templateInputContainer.cloneNode(true);

    // Clear the values of the cloned input container
    newInputContainer.querySelectorAll('select').forEach(function (select) {
        select.selectedIndex = 0;
    });

    // Append the cloned input container to the container
    var container = document.querySelector('.input-pairs');
    container.appendChild(newInputContainer);
}

function populateDropdownOptions(options, elementId) {
    var select = document.getElementById(elementId);
    options.forEach(function(value) {
        var option = document.createElement("option");
        option.value = value;
        option.text = value;
        select.add(option);
    });
}

// Populate day options (1 to 31)
populateDropdownOptions(Array.from({ length: 31 }, (_, i) => i + 1), "start_day");
populateDropdownOptions(Array.from({ length: 31 }, (_, i) => i + 1), "end_day");

months = ['Januar', 'Februar', 'Mart', 'April', 'Maj', 'Jun', 'Jul', 'Avgust', 'Septembar', 'Oktobar', 'Novembar', 'Decembar'];
// Populate month options (1 to 12)
populateDropdownOptions(months, "start_month");
populateDropdownOptions(months, "end_month");

// Populate year options (e.g., from 2022 to 2030)
populateDropdownOptions(Array.from({ length: 9 }, (_, i) => 2024 + i), "start_year");
populateDropdownOptions(Array.from({ length: 9 }, (_, i) => 2024 + i), "end_year");

populateDropdownOptions(Array.from({ length: 24 }, (_, i) => 0 + i), "start_hours");
populateDropdownOptions(Array.from({ length: 24 }, (_, i) => 0 + i), "end_hours");

populateDropdownOptions(Array.from({ length: 60 }, (_, i) => 0 + i), "start_minutes");
populateDropdownOptions(Array.from({ length: 60 }, (_, i) => 0 + i), "end_minutes");
