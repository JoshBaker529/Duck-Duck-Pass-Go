from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pathlib import Path
import time

def getPos():
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")
    options.set_capability("goog:loggingPrefs", {"browser": "ALL"})
    
    # Enable geolocation permission
    options.add_argument("--enable-geolocation")
    options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.geolocation": 1  # 1 = allow, 2 = block
    })
    
    driver = webdriver.Chrome(options=options)
    
    html_file_path = Path("/Users/joshbaker/Projects/test.html")
    driver.get(html_file_path.as_uri())
    # After driver initialization, before loading page
    driver.execute_cdp_cmd("Browser.grantPermissions", {
        "permissions": ["geolocation"],
        "origin": html_file_path.as_uri()
    })
    
    # Give the page time to load
    #time.sleep(1)
    
    # Test geolocation with error handling
    result = driver.execute_async_script("""
        var callback = arguments[arguments.length - 1];
        
        if (!navigator.geolocation) {
            callback({error: 'Geolocation not supported'});
            return;
        }
        
        navigator.geolocation.getCurrentPosition(
            function(position) {
                callback({
                    success: true,
                    latitude: position.coords.latitude,
                    longitude: position.coords.longitude,
                    accuracy: position.coords.accuracy
                });
            },
            function(error) {
                callback({
                    success: false,
                    error: error.message,
                    code: error.code
                });
            },
            { timeout: 5000, enableHighAccuracy: true }
        );
    """)
    driver.quit()
    print(result['latitude'], result['longitude'])
    return (result['latitude'], result['longitude'])

