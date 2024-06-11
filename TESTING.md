# My Fitness Friend - Testing

## Table of Contents

- [Automated testing](#automated-testing)
- [Manual testing](#manual-testing)
  - [Layout](#layout)
  - [Home](#home)
  - [Login](#login)
  - [Register](#register)
  - [Basket](#basket)
  - [Checkout](#checkout)
  - [Food Diary](#food-diary)
  - [Goals](#goals)
  - [Password Reset](#password-reset)
  - [Product Details](#product-details)
  - [Search Products](#search-products)
  - [Store](#store)

## Automated testing

Testing will be partly accomplished by a suite of automated tests. This is the output from a run of the test suite indicating that all tests passed:

```console
PS C:\Users\david\source\repos\my_fitness_friend> python manage.py test
Found 62 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..............................................................
----------------------------------------------------------------------
Ran 62 tests in 30.614s

OK
Destroying test database for alias 'default'...
```

## Manual testing

### Layout

#### My Fitness Friend link works

#### Home link works

#### Log in link works

#### Register link works

#### Log out link works

#### My profile link works

#### Food Diary link works

#### Goals link works

#### Store link works

#### Basket link works

#### Content attribution links work

### Home

[Lighthouse Report](documentation/lighthouse-reports/home.pdf)

#### Go to your food diary link works

#### Go to your goals link works

#### Go to the store link works

### Login

[Lighthouse Report](documentation/lighthouse-reports/login.pdf)

#### Sign up link works

#### Forgot password link works

#### Login Google sign in link works

#### Correct username and password can log in

#### Incorrect username cannot log in

#### Incorrect password cannot log in

### Register

[Lighthouse Report](documentation/lighthouse-reports/register.pdf)

#### Sign in link works

#### Register Google sign in link works

#### Valid input can register

#### Invalid email cannot register

#### Invalid username cannot register

### Basket

[Lighthouse Report](documentation/lighthouse-reports/basket.pdf)

#### Checkout button is disabled when basket is empty

#### Checkout button works when basket has items

### Checkout

[Lighthouse Report](documentation/lighthouse-reports/checkout.pdf)

#### Valid input can checkout

### Food Diary

[Lighthouse Report](documentation/lighthouse-reports/food-diary.pdf)

#### Food diary redirects to login page when user is unauthenticated

#### User can add food to breakfast

#### User can add food to lunch

#### User can add food to dinner

#### User can add food to snacks

#### Totals are calculated correctly

#### Remaining values are calculated correctly

#### Diary for the chosen date is loaded when the chosen date is changed

### Goals

[Lighthouse Report](documentation/lighthouse-reports/goals.pdf)

#### Goals redirects to login page when user is unauthenticated

#### Goal wizard form works

#### Macro goals form works

### Password Reset

[Lighthouse Report](documentation/lighthouse-reports/password-reset.pdf)

#### Password reset redirects to login page when user is unauthenticated

#### Change password form works

#### Link to forgot password works

### Product Details

[Lighthouse Report](documentation/lighthouse-reports/product-details.pdf)

#### Add to basket button works

#### Variant selectors work

#### Price is calculated correctly

### Search Products

[Lighthouse Report](documentation/lighthouse-reports/search-products.pdf)

#### Pagination works

#### Sorting by price low to high works

#### Sorting by price high to low works

#### Items per page selector works

### Store

[Lighthouse Report](documentation/lighthouse-reports/store.pdf)

#### Featured links work
