document.addEventListener("DOMContentLoaded", fetchStates);

function fetchStates() {
    fetch('/states')
        .then(response => response.json())
        .then(states => {
            const stateSelect = document.getElementById("state-select");
            states.forEach(state => {
                const option = document.createElement("option");
                option.value = state;
                option.textContent = state;
                stateSelect.appendChild(option);
            });
        });
}

function fetchDistricts() {
    const state = document.getElementById("state-select").value;
    const districtList = document.getElementById("district-list");
    districtList.innerHTML = ""; // Clear existing districts

    if (state) {
        fetch(`/districts/${state}`)
            .then(response => response.json())
            .then(districts => {
                districts.forEach(district => {
                    const districtDiv = document.createElement("div");
                    districtDiv.classList.add("district");

                    // Populate district details
                    districtDiv.innerHTML = `
                        <h3>${district.name}</h3>
                        <p><strong>Population:</strong> ${district.population}</p>
                        <p><strong>Literacy Rate:</strong> ${district.literacy_rate}%</p>
                        <p><strong>Cases:</strong> ${district.Cases}</p>
                        <p><strong>Mortality Rate:</strong> ${district['Mortality rate']}%</p>
                    `;
                    
                    // Append to district list
                    districtList.appendChild(districtDiv);
                });
            });
    }
}
