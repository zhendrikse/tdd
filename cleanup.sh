find . -name node_modules | xargs rm -rf
find . -name target | xargs rm -rf
find . -name build | xargs rm -rf
find . -name bin | xargs rm -rf
find . -name cljs-out | xargs rm -rf
find . -name obj | xargs rm -rf
find . -name htmlcov | xargs rm -rf
find . -name .coverage | xargs rm -rf
find . -name coverage | xargs rm -rf
find . -name __pycache__ | xargs rm -rf
find . -name .pytest_cache | xargs rm -rf
find . -name .lein-failures | xargs rm -rf
rm -rf tdd-katas/train-reservation/train-reservation-dotnet/TicketOffice.Specs/Features/TrainCancellation.feature.cs
rm -rf tdd-katas/train-reservation/train-reservation-dotnet/TicketOffice.Specs/Features/TrainReservation.feature.cs
