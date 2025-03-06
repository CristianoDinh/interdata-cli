import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TestAPIComponent } from './test-api.component';

describe('TestAPIComponent', () => {
  let component: TestAPIComponent;
  let fixture: ComponentFixture<TestAPIComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TestAPIComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TestAPIComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
