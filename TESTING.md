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

<details>
<summary>Before</summary>

![Before](documentation/images/tests/layout/my-fitness-friend-link-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/layout/my-fitness-friend-link-works/after.jpg)

</details>

#### Home link works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/layout/home-link-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/layout/home-link-works/after.jpg)

</details>

#### Log in link works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/layout/log-in-link-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/layout/log-in-link-works/after.jpg)

</details>

#### Register link works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/layout/register-link-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/layout/register-link-works/after.jpg)

</details>

#### Log out link works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/layout/log-out-link-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/layout/log-out-link-works/after.jpg)

</details>

#### My profile link works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/layout/my-profile-link-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/layout/my-profile-link-works/after.jpg)

</details>

#### Food Diary link works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/layout/food-diary-link-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/layout/food-diary-link-works/after.jpg)

</details>

#### Goals link works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/layout/goals-link-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/layout/goals-link-works/after.jpg)

</details>

#### Store link works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/layout/store-link-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/layout/store-link-works/after.jpg)

</details>

#### Basket link works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/layout/basket-link-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/layout/basket-link-works/after.jpg)

</details>

#### Content attribution links work

<details>
<summary>Before</summary>

![Before](documentation/images/tests/layout/content-attribution-links-work/before1.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/layout/content-attribution-links-work/after1.jpg)

</details>

<br>

<details>
<summary>Before</summary>

![Before](documentation/images/tests/layout/content-attribution-links-work/before2.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/layout/content-attribution-links-work/after2.jpg)

</details>

### Home

[Lighthouse Report](documentation/lighthouse-reports/home.pdf)

#### Go to your food diary link works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/home/go-to-your-food-diary-link-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/home/go-to-your-food-diary-link-works/after.jpg)

</details>

#### Go to your goals link works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/home/go-to-your-goals-link-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/home/go-to-your-goals-link-works/after.jpg)

</details>

#### Go to the store link works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/home/go-to-the-store-link-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/home/go-to-the-store-link-works/after.jpg)

</details>

### Login

[Lighthouse Report](documentation/lighthouse-reports/login.pdf)

#### Sign up link works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/login/sign-up-link-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/login/sign-up-link-works/after.jpg)

</details>

#### Forgot password link works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/login/forgot-password-link-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/login/forgot-password-link-works/after.jpg)

</details>

#### Login Google sign in link works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/login/login-google-sign-in-link-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/login/login-google-sign-in-link-works/after.jpg)

</details>

#### Correct username and password can log in

<details>
<summary>Before</summary>

![Before](documentation/images/tests/login/correct-username-and-password-can-log-in/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/login/correct-username-and-password-can-log-in/after.jpg)

</details>

#### Incorrect username cannot log in

<details>
<summary>Before</summary>

![Before](documentation/images/tests/login/incorrect-username-cannot-log-in/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/login/incorrect-username-cannot-log-in/after.jpg)

</details>

#### Incorrect password cannot log in

<details>
<summary>Before</summary>

![Before](documentation/images/tests/login/incorrect-password-cannot-log-in/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/login/incorrect-password-cannot-log-in/after.jpg)

</details>

### Register

[Lighthouse Report](documentation/lighthouse-reports/register.pdf)

#### Sign in link works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/register/sign-in-link-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/register/sign-in-link-works/after.jpg)

</details>

#### Register Google sign in link works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/register/register-google-sign-in-link-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/register/register-google-sign-in-link-works/after.jpg)

</details>

#### Valid input can register

<details>
<summary>Before</summary>

![Before](documentation/images/tests/register/valid-input-can-register/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/register/valid-input-can-register/after.jpg)

</details>

#### Invalid email cannot register

<details>
<summary>Before</summary>

![Before](documentation/images/tests/register/invalid-email-cannot-register/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/register/invalid-email-cannot-register/after.jpg)

</details>

#### Invalid username cannot register

<details>
<summary>Before</summary>

![Before](documentation/images/tests/register/invalid-username-cannot-register/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/register/invalid-username-cannot-register/after.jpg)

</details>

### Basket

[Lighthouse Report](documentation/lighthouse-reports/basket.pdf)

#### Checkout button is disabled when basket is empty

<details>
<summary>Evidence</summary>

![Evidence](documentation/images/tests/basket/checkout-button-is-disabled-when-basket-is-empty/evidence.jpg)

</details>

#### Checkout button works when basket has items

<details>
<summary>Evidence</summary>

![Evidence](documentation/images/tests/basket/checkout-button-works-when-basket-has-items/evidence.jpg)

</details>

### Checkout

[Lighthouse Report](documentation/lighthouse-reports/checkout.pdf)

#### Valid input can checkout

<details>
<summary>Before</summary>

![Before](documentation/images/tests/checkout/valid-input-can-checkout/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/checkout/valid-input-can-checkout/after.jpg)

</details>

### Food Diary

[Lighthouse Report](documentation/lighthouse-reports/food-diary.pdf)

#### Food diary redirects to login page when user is unauthenticated

<details>
<summary>Before</summary>

![Before](documentation/images/tests/food-diary/food-diary-redirects-to-login-page-when-user-is-unauthenticated/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/food-diary/food-diary-redirects-to-login-page-when-user-is-unauthenticated/after.jpg)

</details>

#### User can add food to breakfast

<details>
<summary>Before</summary>

![Before](documentation/images/tests/food-diary/user-can-add-food-to-breakfast/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/food-diary/user-can-add-food-to-breakfast/after.jpg)

</details>

#### User can add food to lunch

<details>
<summary>Before</summary>

![Before](documentation/images/tests/food-diary/user-can-add-food-to-lunch/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/food-diary/user-can-add-food-to-lunch/after.jpg)

</details>

#### User can add food to dinner

<details>
<summary>Before</summary>

![Before](documentation/images/tests/food-diary/user-can-add-food-to-dinner/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/food-diary/user-can-add-food-to-dinner/after.jpg)

</details>

#### User can add food to snacks

<details>
<summary>Before</summary>

![Before](documentation/images/tests/food-diary/user-can-add-food-to-snacks/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/food-diary/user-can-add-food-to-snacks/after.jpg)

</details>

#### Totals are calculated correctly

<details>
<summary>Evidence</summary>

![Evidence](documentation/images/tests/food-diary/totals-are-calculated-correctly/evidence.jpg)

</details>

#### Remaining values are calculated correctly

<details>
<summary>Evidence</summary>

![Evidence](documentation/images/tests/food-diary/remaining-values-are-calculated-correctly/evidence.jpg)

</details>

#### Diary for the chosen date is loaded when the chosen date is changed

<details>
<summary>Before</summary>

![Before](documentation/images/tests/food-diary/diary-for-the-chosen-date-is-loaded-when-the-chosen-date-is-changed/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/food-diary/diary-for-the-chosen-date-is-loaded-when-the-chosen-date-is-changed/after.jpg)

</details>

### Goals

[Lighthouse Report](documentation/lighthouse-reports/goals.pdf)

#### Goals redirects to login page when user is unauthenticated

<details>
<summary>Before</summary>

![Before](documentation/images/tests/goals/goals-redirects-to-login-page-when-user-is-unauthenticated/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/goals/goals-redirects-to-login-page-when-user-is-unauthenticated/after.jpg)

</details>

#### Goal wizard form works

The goal wizard formula is as follows:

```default
rmr = 10 * weight_kg + 6.25 * height_cm - 5 * age
rmr = rmr + 5 if gender is male
rmr = rmr - 161 if gender is female

rmr = rmr * 1.2 if activity level is sedentary
rmr = rmr * 1.357 if activity level is light
rmr = rmr * 1.55 if activity level is moderate
rmr = rmr * 1.725 if activity level is very active
rmr = rmr * 1.9 if activity level is extra active

goal.calories = rmr if goal is to maintain weight
goal.calories = rmr + 500 if goal is to gain weight
goal.calories = rmr - 500 if goal is to lose weight

weight_pounds = weight_kg * 2.2

goal.protein_grams = int(weight_pounds * 1.5)

protein_calories = goal.protein_grams * 4
remaining_calories = goal.calories - protein_calories
carbs_calories = remaining_calories / 2
fat_calories = remaining_calories / 2

goal.carbs_grams = int(carbs_calories / 4) - 25
goal.fat_grams = int(fat_calories / 9)
goal.sodium_milligrams = 1500
goal.sugar_grams = 25
```

According to this formula, the following input should yield the associated output:

```default
gender = male
weight kg = 77
height cm = 180
age = 32
activity level = moderate
goal = to maintain weight
```

```default
rmr = (10 * 77 + 6.25 * 180 - 5 * 32 + 5) * 1.55 = 2697
weight_pounds = 77 * 2.2 = 169.4
protein_calories = 254 * 4 = 1016
remaining_calories = 2697 - 1016 = 1681
carbs_calories = 1681 / 2 = 840.5
fat_calories = 1681 / 2 = 840.5

calories = 2697
carbs grams = int(840.5 / 4) - 25 = 185
fat grams = int(840.5 / 9) = 93
protein grams = 254
sodium milligrams = 1500
sugar grams = 25
```

<details>
<summary>Before</summary>

![Before](documentation/images/tests/goals/goal-wizard-form-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/goals/goal-wizard-form-works/after.jpg)

</details>

#### Macro goals form works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/goals/macro-goals-form-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/goals/macro-goals-form-works/after.jpg)

</details>

### Product Details

[Lighthouse Report](documentation/lighthouse-reports/product-details.pdf)

#### Add to basket button works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/product-details/add-to-basket-button-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/product-details/add-to-basket-button-works/after.jpg)

</details>

#### Variant selectors work

<details>
<summary>Before</summary>

![Before](documentation/images/tests/product-details/variant-selectors-work/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/product-details/variant-selectors-work/after.jpg)

</details>

#### Price is calculated correctly

<details>
<summary>Evidence</summary>

![Evidence](documentation/images/tests/product-details/price-is-calculated-correctly/evidence.jpg)

</details>

### Search Products

[Lighthouse Report](documentation/lighthouse-reports/search-products.pdf)

#### Pagination works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/search-products/pagination-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/search-products/pagination-works/after.jpg)

</details>

#### Sorting by price low to high works

<details>
<summary>Evidence 1</summary>

![Evidence 1](documentation/images/tests/search-products/sorting-by-price-low-to-high-works/evidence1.jpg)

</details>

<details>
<summary>Evidence 2</summary>

![Evidence 2](documentation/images/tests/search-products/sorting-by-price-low-to-high-works/evidence2.jpg)

</details>

#### Sorting by price high to low works

<details>
<summary>Evidence 1</summary>

![Evidence 1](documentation/images/tests/search-products/sorting-by-price-high-to-low-works/evidence1.jpg)

</details>

<details>
<summary>Evidence 2</summary>

![Evidence 2](documentation/images/tests/search-products/sorting-by-price-high-to-low-works/evidence2.jpg)

</details>

#### Items per page selector works

<details>
<summary>Before 1</summary>

![Before 1](documentation/images/tests/search-products/items-per-page-selector-works/before1.jpg)

</details>

<details>
<summary>Before 2</summary>

![Before 2](documentation/images/tests/search-products/items-per-page-selector-works/before2.jpg)

</details>

<details>
<summary>After 1</summary>

![After 1](documentation/images/tests/search-products/items-per-page-selector-works/after1.jpg)

</details>

<details>
<summary>After 2</summary>

![After 2](documentation/images/tests/search-products/items-per-page-selector-works/after2.jpg)

</details>

### Store

[Lighthouse Report](documentation/lighthouse-reports/store.pdf)

#### Featured links work

<details>
<summary>Before</summary>

![Before](documentation/images/tests/store/featured-links-work/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/store/featured-links-work/after.jpg)

</details>
