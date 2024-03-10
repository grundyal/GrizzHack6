// Example JSON list
var jsonList = [
    {
        "eventSummary": "Event 1 Summary",
        "redditReaction": "Positive reaction to Event 1"
    },
    {
        "eventSummary": "Event 2 Summary",
        "redditReaction": "Mixed reaction to Event 2"
    },
    {
        "eventSummary": "Event 3 Summary",
        "redditReaction": "Negative reaction to Event 3"
    }
    // Add more JSON objects as needed
];

// Function to parse and format JSON objects
function parseAndFormatJson(jsonList) {
    var outputContainer = document.getElementById('output-container');

    jsonList.forEach(function (jsonObject) {
        var jsonContainer = document.createElement('div');
        jsonContainer.classList.add('json-container');

        // Event Summary
        var eventSummaryHeader = document.createElement('h3');
        eventSummaryHeader.textContent = 'Event Summary:';
        jsonContainer.appendChild(eventSummaryHeader);

        var eventSummaryText = document.createElement('p');
        eventSummaryText.textContent = jsonObject.eventSummary;
        jsonContainer.appendChild(eventSummaryText);

        // Reddit Reaction
        var redditReactionHeader = document.createElement('h3');
        redditReactionHeader.textContent = 'Reddit Reaction:';
        jsonContainer.appendChild(redditReactionHeader);

        var redditReactionText = document.createElement('p');
        redditReactionText.textContent = jsonObject.redditReaction;
        jsonContainer.appendChild(redditReactionText);

        // Add a gap between lists
        var gap = document.createElement('hr');
        jsonContainer.appendChild(gap);

        // Append the formatted JSON container to the output container
        outputContainer.appendChild(jsonContainer);
    });
}

// Call the function with the provided JSON list
parseAndFormatJson(jsonList);
