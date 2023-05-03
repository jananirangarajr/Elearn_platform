import { createStore, combineReducers } from 'redux';

// Reducer for username
const usernameReducer = (state = '', action) => {
    switch (action.type) {
        case 'SET_USERNAME':
            return action.payload;
        default:
            return state;
    }
};

// Reducer for user ID
const userIdReducer = (state = '', action) => {
    switch (action.type) {
        case 'SET_USER_ID':
            return action.payload;
        default:
            return state;
    }
};
const userCoursesReducer = (state = {}, action) => {
    switch (action.type) {
        case 'SET_USER_COURSES':
            return action.payload;
        default:
            return state;
    }
};

const coursesReducer = (state = {}, action) => {
    switch (action.type) {
        case 'SET_COURSES':
            return action.payload;
        default:
            return state;
    }
};
// Combine the reducers into a single reducer
const rootReducer = combineReducers({
    username: usernameReducer,
    userId: userIdReducer,
    courses: coursesReducer,
    userCourses: userCoursesReducer
});

// Create the Redux store
const store = createStore(rootReducer);

export default store;
